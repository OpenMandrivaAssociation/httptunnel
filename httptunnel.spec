%define name	httptunnel
%define version	3.3
%define release	%mkrel 11

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Creates bidirectional virtual data connections tunneled through HTTP
License:	GPL
Source0:	ftp://ftp.nocrew.org/pub/nocrew/unix/%{name}-%{version}.tar.bz2
Source1:	hts.xinetd
Source2:	hts.init
Source3:	hts.sysconfig
URL:		http://www.nocrew.org/software/httptunnel.html
Group:		Networking/Other
Requires(post):	rpm-helper
Requires(preun):	rpm-helper
Requires:	xinetd
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
httptunnel creates a bidirectional virtual data path tunneled in HTTP
requests. The HTTP requests can be sent via an HTTP proxy if so desired. 
This can be useful for users behind restrictive firewalls. If WWW access
is allowed through a HTTP proxy, it's possible to use httptunnel and, say,
telnet or PPP to connect to a computer outside the firewall. 

httptunnel is written and maintained by Lars Brinkhoff. See the file
AUTHORS for more information about contributors to this package. 

%prep
%setup -q

%build
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall

install -m 644 %{SOURCE1} -D %{buildroot}%{_sysconfdir}/xinetd.d/hts-xinetd
install -m 755 %{SOURCE2} -D %{buildroot}%{_initrddir}/hts
install -m 644 %{SOURCE3} -D %{buildroot}%{_sysconfdir}/sysconfig/hts

%post
%_post_service hts

%preun
%_preun_service hts

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog DISCLAIMER FAQ HACKING INSTALL NEWS README TODO 
%config(noreplace) %{_sysconfdir}/xinetd.d/hts-xinetd
%config(noreplace) %{_sysconfdir}/sysconfig/hts
%{_initrddir}/hts
%{_bindir}/*
%{_mandir}/man1/*


