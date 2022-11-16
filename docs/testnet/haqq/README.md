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
peers="c24284f77f42a7a9d40f15e67e19bfe64320b5d3@162.55.36.64:26656,fda90bdc36cc35d6a0a74e5de240bcaee72e52bf@195.201.165.123:20116,0c0e74c0550f5c394537f81617a6fd8480381654@94.130.142.27:36656,24da98830276fb0b4fc209cfcaf0cc3a287e1bdd@135.181.222.179:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:35656,ccff2d110a06e8a76fd1529200d96316eb077007@65.108.78.116:46656,6570de868d0f7a5b4dc9f5a007ba98319a7fa8b4@194.163.162.31:26656,ec8a285e36888bd3134266b8ba668b48c327e6bf@142.132.202.50:36656,5c9d40c31c901d034ff19ba51b3465921f291006@135.181.212.21:26656,2b45442c91f25487f0eebe464a1092e2ebda6ddf@195.54.41.148:22656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.haqqd/config/config.toml
```
