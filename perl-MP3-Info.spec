%define modname	MP3-Info
%define modver	1.26

Summary:	Perl module to manipulate / fetch info from MP3 audio files
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	2
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/MP3/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(inc::Module::Install)
BuildRequires:	perl-devel

%description
Manipulate / fetch info from MP3 audio files :	winamp genres, mp3tag, mp3info.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make OPTIMIZE="%{optflags}"

%install
%makeinstall_std

%files
%doc Changes eg META.yml
%{perl_vendorlib}/MP3
%{_mandir}/man3/*

