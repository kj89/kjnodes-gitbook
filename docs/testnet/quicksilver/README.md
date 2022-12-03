# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/quicksilver.png" width="150" alt=""><figcaption></figcaption></figure>

Quicksilver is a permissionless, sovereign Cosmos SDK zone providing liquid staking for the entire Cosmos Ecosystem.

**Chain ID**: innuendo-3 | **Latest Binary Version**: v0.10.3 | **Wasm**: OFF

Website: [https://quicksilver.zone](https://quicksilver.zone)


## Public endpoints

* rpc: [https://quicksilver-testnet.rpc.kjnodes.com](https://quicksilver-testnet.rpc.kjnodes.com)
* api: [https://quicksilver-testnet.api.kjnodes.com](https://quicksilver-testnet.api.kjnodes.com)

## Peering

**state-sync**

```
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@quicksilver-testnet.rpc.kjnodes.com:11656
```

**seed-node**

```
3f472746f46493309650e5a033076689996c8881@quicksilver-testnet.rpc.kjnodes.com:11659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/quicksilver-testnet/addrbook.json > $HOME/.quicksilverd/config/addrbook.json
```

**live-peers** (10)
```
peers="95a1126503bd644746b62bac1d57bd3913044149@144.76.45.59:22656,41f7d7004cace7bd1760a5f980a86123700c8f1d@185.146.148.116:26656,0a3ac40a7a4ce35978c4da97be2eb6974bc3c58b@185.252.233.217:46656,66f9d8f52a4637dc9215cdaa8dc2977633e52bbf@95.217.144.121:26656,125327a98d0e63adfb3f0be513947a96b24231fa@5.161.145.173:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:11656,af8cfa944802a9bd510fc3407950a15e8be86c31@213.239.217.52:30656,f337087c08a4965e6ba6b7fc8813c6abcdafaf88@178.128.228.78:26656,25410bff2fb7312d24c11b1e990507e5e3aa40b7@135.125.5.31:48656,13564ca7ffcc8fa6bcc6d405c96fe8c724ec17da@88.99.213.25:11656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.quicksilverd/config/config.toml
```
