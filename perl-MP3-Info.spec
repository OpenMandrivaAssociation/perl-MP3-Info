%define real_name MP3-Info
%define name perl-%real_name
%define version 1.20
%define release %mkrel 1

Summary: Perl module to manipulate / fetch info from MP3 audio files
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL
Group: Development/Perl
URL: http://search.cpan.org/dist/%{real_name}/
Source: ftp://ftp.pasteur.fr/pub/computing/CPAN/modules/by-module/MPEG/%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildArch: noarch
Buildroot: %{_tmppath}/%{name}-root
Obsoletes: perl-MPEG-MP3Info
Provides: perl-MPEG-MP3Info = %{version}

%description
Manipulate / fetch info from MP3 audio files : winamp genres, mp3tag, mp3info.

%prep
%setup -q -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make OPTIMIZE="$RPM_OPT_FLAGS"
%make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%files
%defattr(-,root,root)
%doc README Changes eg
%{_mandir}/*/*
%{perl_vendorlib}/MP3

%clean
rm -rf $RPM_BUILD_ROOT

