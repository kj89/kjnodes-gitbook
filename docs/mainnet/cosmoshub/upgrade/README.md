---
description: Prepare for and the upcomming chain upgrade using Cosmovisor.
---

# Upgrade

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/cosmoshub.png" width="150" alt=""><figcaption></figcaption></figure>

**Chain ID**: cosmoshub-4 | **Latest Version Tag**: v7.1.0 | **Custom Port**: 34

{% hint style='info' %}
Since we are using Cosmovisor, it makes it very easy to prepare for upcomming upgrade.
You just have to build new binaries and move it into cosmovisor upgrades directory.
{% endhint %}

## Download and build upgrade binaries

```bash
# Clone project repository
cd $HOME
rm -rf gaia
git clone https://github.com/cosmos/gaia.git
cd gaia
git checkout v7.1.0

# Build binaries
make build

# Prepare binaries for Cosmovisor
mkdir -p $HOME/.gaia/cosmovisor/upgrades/v7-Theta/bin
mv build/gaiad $HOME/.gaia/cosmovisor/upgrades/v7-Theta/bin/
rm -rf build
```

*Thats it! Now when upgrade block height is reached, Cosmovisor will handle it automatically!*
