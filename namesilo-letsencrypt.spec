%global debug_package %{nil}

Name:           namesilo-letsencrypt
Version:        0.9.2
Release:        2%{?dist}
Summary:        Automatically generate/renew Let's Encrypt certificates with Certbot on NameSilo DNS

License:        BSD-3-Clause
URL:            https://github.com/ethauvin/namesilo-letsencrypt
Source0:        %{url}/archive/%{version}.tar.gz
Patch0:         config-in-etc.patch

Requires:       python3 python3-tldextract python3-untangle

BuildArch:      noarch

%description
Python scripts (hook) to automate obtaining Let's Encrypt certificates, using
Certbot DNS-01 challenge validation for domains DNS hosted on NameSilo.

%prep
%autosetup -p1

%install
# scripts
mkdir -p %{buildroot}%{_libexecdir}/%{name}
install -Dpm 755 -t %{buildroot}%{_libexecdir}/%{name} authenticator.py cleanup.py

# config
mkdir -p %{buildroot}%{_sysconfdir}/%{name}
install -Dpm 644 -t %{buildroot}%{_sysconfdir}/%{name} config.py

%files
%license LICENSE.txt
%doc README.md
%{_libexecdir}/%{name}/*
%config(noreplace) %{_sysconfdir}/%{name}/*

%changelog
* Tue Jul 30 2024 cyqsimon - 0.9.2-2
- Add python3 as direct dependency
- Build for `noarch`

* Tue Jul 30 2024 cyqsimon - 0.9.2-1
- Release 0.9.2
