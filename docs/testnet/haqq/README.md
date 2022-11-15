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
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:35656,fda90bdc36cc35d6a0a74e5de240bcaee72e52bf@195.201.165.123:20116,adce9d7f72360f6d66c4248b8db8de151b877130@167.235.132.152:26656,ec8a285e36888bd3134266b8ba668b48c327e6bf@142.132.202.50:36656,c24284f77f42a7a9d40f15e67e19bfe64320b5d3@162.55.36.64:26656,0c0e74c0550f5c394537f81617a6fd8480381654@94.130.142.27:36656,562a589b82682f695344bc4a9d7a2fcb5a5a4d80@65.21.60.82:26656,24da98830276fb0b4fc209cfcaf0cc3a287e1bdd@135.181.222.179:26656,ffc8b0dbe8eea3083320cdc014cc6ce8f60e5096@5.161.80.30:12656,ed145a35b436878c1f1c10634bd18600f3696e17@95.217.181.142:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.haqqd/config/config.toml
```
