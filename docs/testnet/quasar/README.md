# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/quasar.png" width="150" alt=""><figcaption></figcaption></figure>

Quasar (pronounced QWAY-ZAR) is a decentralized  appchain enabling interchain digital asset management.

**Chain ID**: qsr-questnet-04 | **Latest Version Tag**: v0.0.2-alpha-11 | **Wasm**: OFF

[Website](https://www.quasar.fi) | [Discord](https://discord.gg/quasarfi) | [Twitter](https://twitter.com/QuasarFi)




## Chain explorer
[https://explorer.kjnodes.com/quasar-testnet](https://explorer.kjnodes.com/quasar-testnet)

## Public endpoints

* api: [https://quasar-testnet.api.kjnodes.com](https://quasar-testnet.api.kjnodes.com)
* rpc: [https://quasar-testnet.rpc.kjnodes.com](https://quasar-testnet.rpc.kjnodes.com)
* grpc: [https://quasar-testnet.grpc.kjnodes.com](https://quasar-testnet.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@quasar-testnet.rpc.kjnodes.com:48656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@quasar-testnet.rpc.kjnodes.com:48659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/quasar-testnet/addrbook.json > $HOME/.quasarnode/config/addrbook.json
```

**live-peers** (18)
```bash
peers="c512c01adb4e88a956918e4f140e44aa408ddd6f@65.21.239.60:25656,a03b3f70544b32d69f322850ad2d0047973b7358@65.109.92.240:17586,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:48656,8937bdacf1f0c8b2d1ffb4606554eaf08bd55df4@5.75.255.107:26656,bf7547ac440b049f7f17db65ab2c54befb9182cc@65.108.238.61:14656,45848bc173bddbf7c685938dfada535ee5a1895b@65.109.23.114:18256,875763b4e1c4f5c2cd9395bf45c4c63eae9aea0f@213.239.217.52:43656,bffb10a5619be7bfa98919e08f4a6bef4f8f6bf0@135.181.210.186:26656,4287c77d9807c53a90853c463891daecf8b1cec1@65.109.57.221:27656,7ba6ff4db4685f5196590825ca5f1a131886811d@213.202.222.182:29656,1cabd0846030da442b347bb17fe02860796d253f@49.12.123.97:16656,7ef67269c8ec37ff8a538a5ae83ca670fd2da686@144.126.135.137:36656,a23f002bda10cb90fa441a9f2435802b35164441@38.146.3.203:18256,b35f3493df8c3be232fe75ef7f4d0cb9d0f59668@65.109.70.23:18256,c7c43689fe3a74d14d8159f80d070c763cbc5a81@96.234.160.22:26656,41ee7632f310c035235828ce03c208dbe1e24d7d@38.146.3.204:18256,eeb4f094eaa62841b4a9a73f0560d6aa1fa87482@65.108.231.124:29656,ade4d8bc8cbe014af6ebdf3cb7b1e9ad36f412c0@176.9.82.221:18256"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quasarnode/config/config.toml
```
