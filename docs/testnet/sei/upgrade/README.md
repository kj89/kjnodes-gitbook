---
description: Prepare for and the upcomming chain upgrade using Cosmovisor.
---

# Upgrade

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/sei.png" width="150" alt=""><figcaption></figcaption></figure>

**Chain ID**: atlantic-2 | **Latest Version Tag**: 2.0.40beta | **Custom Port**: 12

{% hint style='info' %}
Since we are using Cosmovisor, it makes it very easy to prepare for upcomming upgrade.
You just have to build new binaries and move it into cosmovisor upgrades directory.
{% endhint %}

## Download and build upgrade binaries

```bash
# Clone project repository
cd $HOME
rm -rf sei-chain
git clone https://github.com/sei-protocol/sei-chain.git
cd sei-chain
git checkout 2.0.40beta

# Build binaries
make build

# Prepare binaries for Cosmovisor
mkdir -p $HOME/.sei/cosmovisor/upgrades/2.0.40beta/bin
mv build/seid $HOME/.sei/cosmovisor/upgrades/2.0.40beta/bin/
rm -rf build
```

*Thats it! Now when upgrade block height is reached, Cosmovisor will handle it automatically!*
