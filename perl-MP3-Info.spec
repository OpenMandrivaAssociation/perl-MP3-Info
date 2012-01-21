%define upstream_name    MP3-Info
%define upstream_version 1.24

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 3

Summary:    Perl module to manipulate / fetch info from MP3 audio files
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/MP3/%{upstream_name}-%{upstream_version}.tar.gz

BuildArch: noarch
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Manipulate / fetch info from MP3 audio files : winamp genres, mp3tag, mp3info.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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

