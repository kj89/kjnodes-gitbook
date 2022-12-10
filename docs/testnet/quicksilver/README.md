# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/quicksilver.png" width="150" alt=""><figcaption></figcaption></figure>

Quicksilver is a permissionless, sovereign Cosmos SDK zone providing liquid staking for the entire Cosmos Ecosystem.

**Chain ID**: innuendo-3 | **Latest Binary Version**: v0.10.5 | **Wasm**: OFF

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
peers="95a1126503bd644746b62bac1d57bd3913044149@144.76.45.59:22656,af8cfa944802a9bd510fc3407950a15e8be86c31@213.239.217.52:30656,bda5bc971df076b70b4447b842e634948516c5cb@65.108.105.48:14656,8ff8a186fe9cbc70d0f34891fa051f87e561a48b@158.160.0.93:26656,125327a98d0e63adfb3f0be513947a96b24231fa@5.161.145.173:26656,7b21198feaf0882f09fcbb24060961f434d158a3@35.242.163.107:26656,e0f0703e9ce343c46e0ec01b19216715e817b358@65.109.85.170:28656,0a3ac40a7a4ce35978c4da97be2eb6974bc3c58b@185.252.233.217:46656,7d112277450f0a8ef1059e6b334c373a215726ea@23.88.0.170:15619,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:11656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.quicksilverd/config/config.toml
```
