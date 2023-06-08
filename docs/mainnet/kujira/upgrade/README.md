---
description: Prepare for and the upcomming chain upgrade using Cosmovisor.
---

# Upgrade

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/kujira.png" alt=""><figcaption></figcaption></figure>

**Chain ID**: kaiyo-1 | **Latest Version Tag**: v0.8.7 | **Custom Port**: 113

{% hint style='info' %}
Since we are using Cosmovisor, it makes it very easy to prepare for upcomming upgrade.
You just have to build new binaries and move it into cosmovisor upgrades directory.
{% endhint %}

## Download and build upgrade binaries

```bash
# Clone project repository
cd $HOME
rm -rf core
git clone https://github.com/Team-Kujira/core.git
cd core
git checkout v0.8.7

# Build binaries
make build

# Prepare binaries for Cosmovisor
mkdir -p $HOME/.kujira/cosmovisor/upgrades/v0.8.4/bin
mv build/kujirad $HOME/.kujira/cosmovisor/upgrades/v0.8.4/bin/
rm -rf build
```

*Thats it! Now when upgrade block height is reached, Cosmovisor will handle it automatically!*
