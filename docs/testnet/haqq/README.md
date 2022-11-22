# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/haqq.png" width="150" alt=""><figcaption></figcaption></figure>

Haqq is the blockchain network that issues Islamic Coin,  its native cryptocurrency. Haqq is fast, trusted and  compatible with thousands of applications around the world.

**Chain ID**: haqq_54211-3 | **Latest Version Tag**: v1.2.1 | **Wasm**: OFF

Website: [https://islamiccoin.net](https://islamiccoin.net)


## Public endpoints

* rpc: [https://haqq-testnet.rpc.kjnodes.com](https://haqq-testnet.rpc.kjnodes.com)
* api: [https://haqq-testnet.api.kjnodes.com](https://haqq-testnet.api.kjnodes.com)

## Peering

**state-sync**

```
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@haqq-testnet.rpc.kjnodes.com:35656
```

**seed-node**

```
3f472746f46493309650e5a033076689996c8881@haqq-testnet.rpc.kjnodes.com:35659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/haqq-testnet/addrbook.json > $HOME/.haqqd/config/addrbook.json
```

**live-peers** (10)
```
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:35656,dc54dbb3a1ac07a6b04b9d911a80852d41247a48@65.108.198.42:26656,1b9b907b4bf609c7acf47a20bd23320c9e73b784@135.181.222.185:26656,9af0d63f02475fc5c4cf60723070ea735895b626@185.119.59.223:26656,b9d04ade732a3bb91b91e279c36c6f2c12d522d3@109.107.187.78:26656,de231cd155362b2687dca190a744bf839ce4ce63@23.88.112.123:26656,001eb7a3a03dc11539541737262c4ddc84dec283@91.195.101.98:26656,a3e587b8ac1ee3a1563b43388d2bd475c890a6c0@65.109.81.240:26656,ec8a285e36888bd3134266b8ba668b48c327e6bf@142.132.202.50:36656,47a269c3e30f70d8234a2afd8e9055e74129fde0@65.108.129.29:36656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.haqqd/config/config.toml
```
