%define upstream_name    Hash-Rename
%define upstream_version 2.00

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Rename hash keys

License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Hash/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Test::Compile)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(UNIVERSAL::require)
BuildRequires:	perl(Module::Build::Tiny)
BuildRequires:	perl(TAP::Harness::Env)
BuildRequires:	perl(Test::Differences)
BuildArch:	noarch

%description
Using this module you can rename a hash's keys in place.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot}

%check
./Build test

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*
