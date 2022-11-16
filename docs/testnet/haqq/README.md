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
peers="ec8a285e36888bd3134266b8ba668b48c327e6bf@142.132.202.50:36656,b8740983bc275b91a67c1da0b308ddd69167d0ce@185.144.99.231:26656,2b45442c91f25487f0eebe464a1092e2ebda6ddf@195.54.41.148:22656,24da98830276fb0b4fc209cfcaf0cc3a287e1bdd@135.181.222.179:26656,2d13d679b64e1a574904a140f72815644ec71131@65.21.133.125:30656,24cee16ef3d1fa790a4f07212974047369a3e969@198.204.255.156:26656,9af0d63f02475fc5c4cf60723070ea735895b626@185.119.59.223:26656,ed145a35b436878c1f1c10634bd18600f3696e17@95.217.181.142:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:35656,306ce653d6f0c77936b681d4ee8bbf66a4b8bb75@88.208.57.200:60956"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.haqqd/config/config.toml
```
