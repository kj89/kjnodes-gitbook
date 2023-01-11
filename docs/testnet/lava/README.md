# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/lava.png" width="150" alt=""><figcaption></figcaption></figure>

Lava powers a trustless market for RPC data access. The protocol  governs over peer to peer and private Provider-Application pairings,  ensuring high quality RPC service while creating consensus around data served.

**Chain ID**: lava-testnet-1 | **Latest Version Tag**: v0.4.3 | **Wasm**: OFF

[Website](https://lavanet.xyz) | [Discord](https://discord.com/invite/Tbk5NxTCdA) | [Twitter](https://twitter.com/lavanetxyz)


## Public endpoints

* rpc: [https://lava-testnet.rpc.kjnodes.com](https://lava-testnet.rpc.kjnodes.com)
* api: [https://lava-testnet.api.kjnodes.com](https://lava-testnet.api.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@lava-testnet.rpc.kjnodes.com:44656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@lava-testnet.rpc.kjnodes.com:44659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/lava-testnet/addrbook.json > $HOME/.lava/config/addrbook.json
```

**live-peers** (16)
```bash
peers="97b3648ef143d537e6aee3b11f054a0e6b6be691@51.91.144.243:26656,910c0e9e8299d642208ef4c4199ae9ea44d6ffe1@164.68.99.218:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656,3c47fd1662bcb17a4713c23e41d7b25e34478b8e@103.19.25.157:26672,863c2d0946c1df75335e14c53f8c0d525d545225@84.46.245.176:26656,ade02cddf71489b79a2054a7c6ba2cab8a0abb18@185.163.125.232:26656,eb7832932626c1c636d16e0beb49e0e4498fbd5e@65.108.231.124:20656,c83d7b205b2e80bd9a33c13161bd39d520988455@38.242.139.189:26656,4877ad7cf06e277399808d8130a8f25a780a52b0@207.148.122.124:26656,2ec5dc5b90e6c200cbfd4b53c90c0c5d55c33914@139.59.189.24:26656,4ff173846016b0eb92afa5194dfe9e687ec2401d@85.192.48.209:26656,e1d77de8252dc3eb36ee8e70920479a0f990c1e4@95.161.216.107:26656,3a445bfdbe2d0c8ee82461633aa3af31bc2b4dc0@3.252.219.158:26656,3b50e7040fed9e6da907078e8eefa8585fdfd50c@65.108.9.164:37656,8764cd1551dd8da6e1f4a7253a634f1e2a01e351@38.242.199.123:26656,4b0b69e769d303412a5daaa6cc261165c9b92625@75.119.144.1:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
