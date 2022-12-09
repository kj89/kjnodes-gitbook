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
peers="0a3ac40a7a4ce35978c4da97be2eb6974bc3c58b@185.252.233.217:46656,af8cfa944802a9bd510fc3407950a15e8be86c31@213.239.217.52:30656,646e10a81b1e3e188deb32dbb5d39d649aff7025@95.214.52.138:26676,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:11656,884919e20a71dc0c632739f44275897f80725159@185.16.39.51:11656,47a7fac621a79649519eadbb8deb92d33bb3259b@161.97.82.203:26256,a37474c1f254cd4b16d924327a755c914e8e7d86@65.109.30.53:26656,c9a74cdd754a8ccc9243ac2b245e4caaa78695aa@45.85.147.96:26656,95a1126503bd644746b62bac1d57bd3913044149@144.76.45.59:22656,125327a98d0e63adfb3f0be513947a96b24231fa@5.161.145.173:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.quicksilverd/config/config.toml
```
