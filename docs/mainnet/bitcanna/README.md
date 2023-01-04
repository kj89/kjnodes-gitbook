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
peers="1b01a388eaba8f15634c1e5cd5bb7c55810250d2@135.181.219.115:27656,be87c9abf1c54e1cc2f37e68d21fcd61679abb4c@65.21.196.90:46656,c38376851f76a488bcc464ce9e248d6cf2956ba8@176.9.188.21:50656,3b6d207fb9771473771abb4a93385cd642fa7b12@151.80.78.132:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:42656,8a210f1bcfc9015a7bc18dcc5add29c0dce3f2dc@135.181.173.65:26656,2235f1e518c5ea4a412f9dece386348eda356916@66.42.50.244:26656,5bb0a042e8a4ee28bcda1e26148e57787e75a42e@23.88.69.22:28466,90ee680b1738344354c48c23ba1e1fd68e071d80@142.132.248.138:26696,4e1c2471efb89239fb04a4b75f9f87177fd91d00@95.217.151.241:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.bcna/config/config.toml
```
