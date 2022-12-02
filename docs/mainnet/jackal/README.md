# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/jackal.png" width="150" alt=""><figcaption></figcaption></figure>

The Jackal Protocol is a fast, scalable, and secure blockchain that empowers  individuals, developers, and enterprises to increase their data privacy and  cybersecurity posture without sacrificing ease of use. This protocol strives  to offer world-class applications to protect the planet's most important data–your data.

**Chain ID**: jackal-1 | **Latest Version Tag**: v1.1.2-hotfix | **Wasm**: ON

Website: [https://jackalprotocol.com](https://jackalprotocol.com)

## Restake

[Restake with kjnodes](https://restake.app/jackal/jklvaloper1tr3wm3mdkz0tda6t7vavqnn7fe2g4un0f67xmt) (every day at 08:00, 20:00)
## Public endpoints

* rpc: [https://jackal.rpc.kjnodes.com](https://jackal.rpc.kjnodes.com)
* api: [https://jackal.api.kjnodes.com](https://jackal.api.kjnodes.com)

## Peering

**state-sync**

```
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@jackal.rpc.kjnodes.com:37656
```

**seed-node**

```
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@jackal.rpc.kjnodes.com:37659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/jackal/addrbook.json > $HOME/.canine/config/addrbook.json
```

**live-peers** (10)
```
peers="7751d16cfa48da0a5bea6f40e9bcc386b4c76c50@51.89.7.184:26638,fc905fe58d36875a833202ce53759d0ae6c11435@141.95.65.26:48656,0b8bbc839c20b07ac5999bca7d905d53274c5f2d@24.158.14.214:36656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:37656,c2842c76779913e05fa4256e3caab852e1782951@202.61.194.254:60756,46d4495643f2579573a61e181a88de3b8f0acc4f@2.139.23.24:36656,0985977a794b298e7ef990fe344d572c60c453b1@172.105.72.158:26656,9c149b35243970e1f8e0519f1f33f79f7d5bd91b@51.38.52.188:26638,753d35e39ad1f6f2fbf0f406a0c4f2bee3c4c7d0@135.181.153.228:56656,0841db0ae5e5443905837e196d2e1ffd31f2e480@131.153.202.81:36656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.canine/config/config.toml
```
