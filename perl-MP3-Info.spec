%define upstream_name    MP3-Info
%define upstream_version 1.24

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Perl module to manipulate / fetch info from MP3 audio files
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/MP3/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
Manipulate / fetch info from MP3 audio files : winamp genres, mp3tag, mp3info.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make OPTIMIZE="%{optflags}"

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes eg
%{_mandir}/*/*
%{perl_vendorlib}/MP3

%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.240.0-4mdv2012.0
+ Revision: 765495
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.240.0-3
+ Revision: 763990
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.240.0-2
+ Revision: 667245
- mass rebuild

* Tue Jul 07 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.240.0-1mdv2010.1
+ Revision: 393273
- renamed source: in source0: to align on common template
- update to 1.24
- using %%perl_convert_version
- fixed license field

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.23-2mdv2009.0
+ Revision: 223845
- rebuild

* Tue Jan 29 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.23-1mdv2008.1
+ Revision: 159899
- new version

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Apr 29 2007 Olivier Thauvin <nanardon@mandriva.org> 1.22-1mdv2008.0
+ Revision: 19211
- 1.22


* Tue Mar 07 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.20-1mdk
- 1.20

* Fri Apr 22 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.13-1mdk
- 1.13

* Tue Jan 18 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.11-1mdk
- new version 1.11

* Mon Jan 10 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.10-1mdk
- new version 1.10
- Add examples in documentation

* Wed Feb 25 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 1.02-4mdk
- rebuild
- own dir

* Wed Aug 13 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.02-3mdk
- rebuild for new perl
- drop Prefix tag
- don't use PREFIX
- use %%makeinstall_std macro

* Tue May 27 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.02-2mdk
- rebuild for new auto{prov,req}

* Fri Apr 18 2003 François Pons <fpons@mandrakesoft.com> 1.02-1mdk
- 1.02.

