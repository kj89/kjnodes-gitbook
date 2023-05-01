---
description: Prepare for and the upcomming chain upgrade using Cosmovisor.
---

# Upgrade

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/uptick.png" alt=""><figcaption></figcaption></figure>

**Chain ID**: uptick_7000-2 | **Latest Version Tag**: v0.2.6 | **Custom Port**: 115

{% hint style='info' %}
Since we are using Cosmovisor, it makes it very easy to prepare for upcomming upgrade.
You just have to build new binaries and move it into cosmovisor upgrades directory.
{% endhint %}

## Download and build upgrade binaries

```bash
# Clone project repository
cd $HOME
rm -rf uptick
git clone https://github.com/UptickNetwork/uptick.git
cd uptick
git checkout v0.2.6

# Build binaries
make build

# Prepare binaries for Cosmovisor
mkdir -p $HOME/.uptickd/cosmovisor/upgrades/v0.2.6/bin
mv build/uptickd $HOME/.uptickd/cosmovisor/upgrades/v0.2.6/bin/
rm -rf build
```

*Thats it! Now when upgrade block height is reached, Cosmovisor will handle it automatically!*
