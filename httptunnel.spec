%define name	httptunnel
%define version	3.3
%define release	17

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Creates bidirectional virtual data connections tunneled through HTTP
License:	GPL
Source0:	ftp://ftp.nocrew.org/pub/nocrew/unix/%{name}-%{version}.tar.bz2
Source1:	hts.xinetd
Source2:	hts.init
Source3:	hts.sysconfig
URL:		https://www.nocrew.org/software/httptunnel.html
Group:		Networking/Other
Requires(pre):	rpm-helper
Requires(post):	rpm-helper
Requires(preun):	rpm-helper
Requires(postun):	rpm-helper
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
install -d -m 755 %{buildroot}%{_var}/run/%{name}

%pre
%_pre_useradd %{name} %{_var}/run/%{name} /bin/false

%post
%_post_service hts

%preun
%_preun_service hts

%postun
%_postun_userdel %{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog DISCLAIMER FAQ HACKING INSTALL NEWS README TODO 
%config(noreplace) %{_sysconfdir}/xinetd.d/hts-xinetd
%config(noreplace) %{_sysconfdir}/sysconfig/hts
%{_initrddir}/hts
%attr(-,httptunnel,httptunnel) %{_var}/run/%{name}
%{_bindir}/*
%{_mandir}/man1/*


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 3.3-16mdv2011.0
+ Revision: 619490
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 3.3-15mdv2010.0
+ Revision: 429479
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 3.3-14mdv2009.0
+ Revision: 247074
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 3.3-12mdv2008.1
+ Revision: 140755
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - better init script
      run under a specific uid
      fix pid file issue


* Sun Jan 21 2007 Olivier Blin <oblin@mandriva.com> 3.3-11mdv2007.0
+ Revision: 111327
- use LSB header in initscript
- bunzip2 sources
- Import httptunnel

* Wed Aug 30 2006 Guillaume Rousse <guillomovitch@mandriva.org> 3.3-10mdv2007.0
- Rebuild

* Wed Nov 02 2005 Guillaume Rousse <guillomovitch@mandriva.org> 3.3-9mdk
- %%mkrel
- spec cleanup
- fix requires
- don't mark init script as config

* Thu Oct 28 2004 Guillaume Rousse <guillomovitch@mandrake.org> 3.3-8mdk 
- distinct name for xinetd service (fix bug #11237)
- no restart on upgrade, as there is policy about it

* Thu Jul 22 2004 Guillaume Rousse <guillomovitch@mandrake.org> 3.3-7mdk 
- rpmbuildupdate aware

