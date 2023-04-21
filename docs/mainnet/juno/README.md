# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/juno.png" width="150" alt=""><figcaption></figcaption></figure>

Juno is a global, open source, permission-less  network for decentralized interoperable applications.

**Chain ID**: juno-1 | **Latest Version Tag**: v14.0.0 | **Wasm**: ON

[Website](https://www.junonetwork.io) | [Discord](https://discord.gg/qJxgUSGHbb) | [Twitter](https://twitter.com/JunoNetwork)



Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/juno](https://explorer.kjnodes.com/juno)

## Public endpoints

* api: [https://juno.api.kjnodes.com](https://juno.api.kjnodes.com)
* rpc: [https://juno.rpc.kjnodes.com](https://juno.rpc.kjnodes.com)
* grpc: juno.grpc.kjnodes.com:57090

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@juno.rpc.kjnodes.com:57656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@juno.rpc.kjnodes.com:57659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/juno/addrbook.json > $HOME/.juno/config/addrbook.json
```

**live-peers** (10)
```bash
peers="2832bdb0a1bdddb2b17d1229a799290222c085d0@135.125.189.131:33095,a3bdae642a2ac5b7091a9b690eda8d59ad523795@167.99.128.187:26656,ae1b388ee37b03d0eb292342341e969de695c427@65.108.235.34:2000,5292be1e0829141ce28e01de3234a2060d592802@198.244.176.186:36656,45f4da091b7f7536c3e0182083ff2326d0c3be6a@66.85.137.122:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:57656,471518432477e31ea348af246c0b54095d41352c@88.198.131.120:26656,82588f011491c6100d922d133f52fc23460b9231@95.217.91.232:26656,97e4468ac589eac505a800411c635b14511a61bb@5.9.239.232:26656,3ee2034cf0180e4d50f7b3ed952472add3316faf@88.99.164.158:1066"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.juno/config/config.toml
```
