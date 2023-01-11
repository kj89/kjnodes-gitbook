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

**live-peers** (20)
```bash
peers="32e448800e1deb520a9a734c361cdfc3e3958f2f@86.48.1.143:26656,3b50e7040fed9e6da907078e8eefa8585fdfd50c@65.108.9.164:37656,377370216f2c003b9d00118ec5373ed21f13aab3@185.16.39.19:35656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656,eb7832932626c1c636d16e0beb49e0e4498fbd5e@65.108.231.124:20656,d927303d07abf24b72f3eb8ae495ac02372e3908@91.195.101.78:26656,7c1b4625e9be15151bd4c977140aa3fe601f0456@65.108.97.58:2996,3c47fd1662bcb17a4713c23e41d7b25e34478b8e@103.19.25.157:26672,837371bcb3206bbaffb5b3ced32cb7d65366cf81@212.3.132.244:26656,c506970f0ac6e99ba3e1e01da33a39315c8b7aa1@38.242.141.94:26656,99327e5cf0f31ac3bb1ca8e39cc9f17c823b7ec1@109.236.88.8:26656,3d7f24398295c769b629180f897620943a56761a@103.158.36.28:26656,3a445bfdbe2d0c8ee82461633aa3af31bc2b4dc0@3.252.219.158:26656,a7944b8f0953e703d301670a9aa5312f3edf8cf4@65.109.106.91:24656,12d6fc425a5d3c8164b41b6f5ea28168ae56f4ba@178.18.246.21:26656,e593c7a9ca61f5616119d6beb5bd8ef5dd28d62d@34.246.190.1:26656,3d4e0eecbbe713a42e785ac1e66ac8ad149b2c4d@164.92.120.104:26656,433be6210ad6350bebebad68ec50d3e0d90cb305@217.13.223.167:60856,c259b7f601ad04654d6104c2aa9001896c975c20@45.76.159.172:26656,6b209fb04491938b4d60b2847340799fbaced19f@38.242.153.36:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
