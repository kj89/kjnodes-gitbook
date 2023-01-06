---
description: Prepare for and the upcomming chain upgrade using Cosmovisor.
---

# Upgrade

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/sei.png" width="150" alt=""><figcaption></figcaption></figure>

**Chain ID**: atlantic-1 | **Latest Version Tag**: 1.2.2beta-postfix | **Custom Port**: 12

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
git checkout 1.2.2beta-postfix

# Build binaries
make build
mkdir -p $HOME/.sei/cosmovisor/upgrades/1.2.2beta-postfix/bin
mv build/seid $HOME/.sei/cosmovisor/upgrades/1.2.2beta-postfix/bin/
rm -rf build
```

*Thats it! Now when upgrade block height is reached, Cosmovisor will handle it automatically!*
