---
description: Prepare for and the upcomming chain upgrade using Cosmovisor.
---

# Upgrade

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/bitcanna.png" alt=""><figcaption></figcaption></figure>

**Chain ID**: bitcanna-1 | **Latest Version Tag**: v1.7.0 | **Custom Port**: 142

{% hint style='info' %}
Since we are using Cosmovisor, it makes it very easy to prepare for upcomming upgrade.
You just have to build new binaries and move it into cosmovisor upgrades directory.
{% endhint %}

## Download and build upgrade binaries

```bash
# Clone project repository
cd $HOME
rm -rf bcna
git clone https://github.com/BitCannaGlobal/bcna.git
cd bcna
git checkout v1.7.0

# Build binaries
make build

# Prepare binaries for Cosmovisor
mkdir -p $HOME/.bcna/cosmovisor/upgrades/vigorous-grow-huckleberry/bin
mv build/bcnad $HOME/.bcna/cosmovisor/upgrades/vigorous-grow-huckleberry/bin/
rm -rf build
```

*Thats it! Now when upgrade block height is reached, Cosmovisor will handle it automatically!*
