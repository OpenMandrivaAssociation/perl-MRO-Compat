%define module	MRO-Compat
%define name	perl-%{module}
%define version 0.04
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	mro::* interface compatibility for Perls < 5.9.5
URL:		http://search.cpan.org/dist/%{module}
Source:		http://search.cpan.org/CPAN/authors/id/B/BL/BLBLACK/%{module}-%{version}.tar.gz
License:	GPL
Group:		Development/Perl
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl(Module::AutoInstall)
BuildRequires:	perl(Class::C3) >= 0.19
BuildRequires:	perl(Class::C3::XS) >= 0.19
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
The "mro" namespace provides several utilities for dealing with method
resolution order and method caching in general in Perl 5.9.5 and higher.

This module provides those interfaces for earlier versions of Perl (back to
5.6.0 anyways).

It is a harmless no-op to use this module on 5.9.5+. If you're writing a piece
of software that would like to use the parts of 5.9.5+'s mro:: interfaces that
are supported here, and you want compatibility with older Perls, this is the
module for you.

Some parts of this interface will work better with Class::C3::XS installed, but
it's not a requirement.

This module never exports any functions. All calls must be fully qualified with
the mro:: prefix.

The interface documentation here serves only as a quick reference of what the
function basically does, and what differences between MRO::Compat and 5.9.5+
one should look out for. The main docs in 5.9.5's mro are the real interface
docs, and contain a lot of other

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
%make test

%install
%{__rm} -rf %{buildroot}
%makeinstall_std

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog README
%{perl_vendorlib}/MRO
%{_mandir}/*/*

