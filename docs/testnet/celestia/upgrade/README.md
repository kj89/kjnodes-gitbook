---
description: Prepare for and the upcomming chain upgrade using Cosmovisor.
---

# Upgrade

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/celestia.png" width="150" alt=""><figcaption></figcaption></figure>

**Chain ID**: mocha | **Latest Version Tag**: v0.11.0 | **Custom Port**: 20

{% hint style='info' %}
Since we are using Cosmovisor, it makes it very easy to prepare for upcomming upgrade.
You just have to build new binaries and move it into cosmovisor upgrades directory.
{% endhint %}

## Download and build upgrade binaries

```bash
# Clone project repository
cd $HOME
rm -rf celestia-app
git clone https://github.com/celestiaorg/celestia-app.git
cd celestia-app

# Build binaries
git checkout v0.11.0
make build
mkdir -p $HOME/.celestia-app/cosmovisor/upgrades/genesis/bin
mv build/celestia-appd $HOME/.celestia-app/cosmovisor/upgrades/genesis/bin/
rm -rf build
```

*Thats it! Now when upgrade block height is reached, Cosmovisor will handle it automatically!*
