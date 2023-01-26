# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/kujira.png" width="150" alt=""><figcaption></figcaption></figure>

Kujira is a Layer 1 protocol built on Cosmos, which can be used for  hosting community-selected projects.

**Chain ID**: kaiyo-1 | **Latest Version Tag**: v0.7.1 | **Wasm**: ON

[Website](https://kujira.app) | [Discord](https://discord.gg/teamkujira) | [Twitter](https://twitter.com/TeamKujira)

## Restake

[Restake with kjnodes](https://restake.app/kujira/kujiravaloper1tnuqj73jfn3724lqz34c27tuv80nv336sadqym) (every day at 08:00, 20:00)
## Chain explorer
[https://explorer.kjnodes.com/kujira](https://explorer.kjnodes.com/kujira)

## Public endpoints

* api: [https://kujira.api.kjnodes.com](https://kujira.api.kjnodes.com)
* rpc: [https://kujira.rpc.kjnodes.com](https://kujira.rpc.kjnodes.com)
* grpc: [https://kujira.grpc.kjnodes.com](https://kujira.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@kujira.rpc.kjnodes.com:13656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@kujira.rpc.kjnodes.com:13659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/kujira/addrbook.json > $HOME/.kujira/config/addrbook.json
```

**live-peers** (10)
```bash
peers="66778cba932969c95117cf720c1ad820fdc68ff5@65.108.235.34:26656,213dbb8301ce1c0f5662a9b723bd613f15e1dd4e@75.119.157.167:30656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656,de08e6178779ff3b19a8b6d22a05664392cb2b35@185.216.179.205:26656,b12591db8b67f7a78b2834b5c122299fdb6c8deb@65.108.201.154:2060,26d19e5b3f3a5ebafe827dabca4ef008d9c5e6fd@168.119.15.94:26656,a9a4c977ec9f4bf907ce4dc74546de166bb40497@51.81.208.63:26656,b80cf7882c8cab4894d41ccd4f5a00406d8b5f7d@146.59.52.48:30095,97e4468ac589eac505a800411c635b14511a61bb@5.9.239.238:26656,fa57c7c253be46ad9f696ee2f2c1d72cbc6a1591@146.59.52.135:31095"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
