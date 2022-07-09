%define modname	MRO-Compat
%define modver	0.15

Summary:	mro::* interface compatibility for Perls < 5.9.5
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	1
License:	GPLv2
Group:		Development/Perl
Url:		http://metacpan.org/pod/MRO::Compat
Source0:	http://search.cpan.org/CPAN/authors/id/H/HA/HAARG/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Module::AutoInstall)
BuildRequires:	perl(Class::C3) >= 0.19
BuildRequires:	perl(Class::C3::XS) >= 0.19
BuildRequires:	perl-devel

%description
The "mro" namespace provides several utilities for dealing with method
resolution order and method caching in general in Perl 5.9.5 and higher.

This module provides those interfaces for earlier versions of Perl
(back to 5.6.0 anyways).

It is a harmless no-op to use this module on 5.9.5+. If you're
writing a piece of software that would like to use the parts of 5.9.5+'s
mro::	interfaces that are supported here, and you want compatibility with
older Perls, this is the module for you.

Some parts of this interface will work better with Class::C3::XS installed,
but it's not a requirement.

This module never exports any functions. All calls must be fully
qualified with the mro:: prefix.

The interface documentation here serves only as a quick reference of what
the function basically does, and what differences between MRO::Compat and
5.9.5+ one should look out for. The main docs in 5.9.5's mro are the real
interface docs, and contain a lot of other

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README
%{perl_vendorlib}/MRO
%{_mandir}/man3/*
