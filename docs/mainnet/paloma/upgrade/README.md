---
description: Prepare for and the upcomming chain upgrade using Cosmovisor.
---

# Upgrade

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/paloma.png" alt=""><figcaption></figcaption></figure>

**Chain ID**: messenger | **Latest Version Tag**: v1.1.0 | **Custom Port**: 110

{% hint style='info' %}
Since we are using Cosmovisor, it makes it very easy to prepare for upcomming upgrade.
You just have to build new binaries and move it into cosmovisor upgrades directory.
{% endhint %}

## Download and build upgrade binaries

```bash
# Clone project repository
cd $HOME
rm -rf paloma
git clone https://github.com/palomachain/paloma.git
cd paloma
git checkout v1.1.0

# Build binaries
make build

# Prepare binaries for Cosmovisor
mkdir -p $HOME/.paloma/cosmovisor/upgrades/v1.1.0/bin
mv build/palomad $HOME/.paloma/cosmovisor/upgrades/v1.1.0/bin/
rm -rf build
```

*Thats it! Now when upgrade block height is reached, Cosmovisor will handle it automatically!*
