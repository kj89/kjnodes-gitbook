---
description: Prepare for and the upcomming chain upgrade using Cosmovisor.
---

# Upgrade

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/juno.png" alt=""><figcaption></figcaption></figure>

**Chain ID**: juno-1 | **Latest Version Tag**: v14.0.0 | **Custom Port**: 157

{% hint style='info' %}
Since we are using Cosmovisor, it makes it very easy to prepare for upcomming upgrade.
You just have to build new binaries and move it into cosmovisor upgrades directory.
{% endhint %}

## Download and build upgrade binaries

```bash
# Clone project repository
cd $HOME
rm -rf juno
git clone https://github.com/CosmosContracts/juno.git
cd juno
git checkout v14.0.0

# Build binaries
make build

# Prepare binaries for Cosmovisor
mkdir -p $HOME/.juno/cosmovisor/upgrades/v14/bin
mv bin/junod $HOME/.juno/cosmovisor/upgrades/v14/bin/
rm -rf build
```

*Thats it! Now when upgrade block height is reached, Cosmovisor will handle it automatically!*
