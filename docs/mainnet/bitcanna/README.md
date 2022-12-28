# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/bitcanna.png" width="150" alt=""><figcaption></figcaption></figure>

BitCanna is a proof-of-stake (POS) decentralized payment network designed exclusively to serve the cannabis industry. 

**Chain ID**: bitcanna-1 | **Latest Version Tag**: v1.5.3 | **Wasm**: OFF

[Website](https://www.bitcanna.io) | [Discord](https://discord.gg/9AVrzaVQvs) | [Twitter](https://twitter.com/BitCannaGlobal)


## Public endpoints

* rpc: [https://bitcanna.rpc.kjnodes.com](https://bitcanna.rpc.kjnodes.com)
* api: [https://bitcanna.api.kjnodes.com](https://bitcanna.api.kjnodes.com)

## Peering

**state-sync**

```
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@bitcanna.rpc.kjnodes.com:42656
```

**seed-node**

```
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@bitcanna.rpc.kjnodes.com:42659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/bitcanna/addrbook.json > $HOME/.bcna/config/addrbook.json
```

**live-peers** (10)
```
peers="4e1c2471efb89239fb04a4b75f9f87177fd91d00@95.217.151.241:26656,89757803f40da51678451735445ad40d5b15e059@169.155.168.66:26656,a9f839c6e24221fb093f13ee41a0af842378fec5@94.130.12.22:26642,90ee680b1738344354c48c23ba1e1fd68e071d80@142.132.248.138:26696,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:42656,43f8f9eee8fe7de19e958edb4e95185ab40f8e39@65.108.238.104:13056,1b01a388eaba8f15634c1e5cd5bb7c55810250d2@135.181.219.115:27656,4dabde84771e8689403ce7c8b76d27e555ab2f00@65.21.136.170:50656,7eba6089dd06147b7993979f901d212e722c21c3@24.158.14.212:36656,c38a5912b4b0f827732862594671c65ad0059932@172.105.196.25:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.bcna/config/config.toml
```
