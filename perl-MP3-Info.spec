%define module MP3-Info
%define name perl-%module
%define version 1.23
%define release %mkrel 2

Name:       %{name}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Perl module to manipulate / fetch info from MP3 audio files
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/MP3/%{module}-%{version}.tar.gz
BuildArch:  noarch
Buildroot:  %{_tmppath}/%{name}-%{version}

%description
Manipulate / fetch info from MP3 audio files : winamp genres, mp3tag, mp3info.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make OPTIMIZE="$RPM_OPT_FLAGS"

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes eg
%{_mandir}/*/*
%{perl_vendorlib}/MP3

