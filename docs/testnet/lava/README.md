# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/lava.png" width="150" alt=""><figcaption></figcaption></figure>

Lava powers a trustless market for RPC data access. The protocol  governs over peer to peer and private Provider-Application pairings,  ensuring high quality RPC service while creating consensus around data served.

**Chain ID**: lava-testnet-1 | **Latest Version Tag**: v0.4.0 | **Wasm**: OFF

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

**live-peers** (23)
```bash
peers="d5e983cb8ad86a3d7d6dd0bc91e969cc8d416c7c@217.76.58.177:26656,c80f5f3b6828342ed2c38026eede1f59b466d30f@168.119.124.130:47656,6d370f3301a19cd4d1788172d8d1dbfd506eac4e@89.252.21.37:26656,66aa428bb00fa1df531ae9ba1b5ab03f6927298e@84.46.249.65:26656,33488cb19cd369d6b28a6263ead2e30f5dedd098@206.189.85.32:26656,2c097870ec04af4177def39cb821c49bd0069b6c@165.232.146.62:26656,e8256f9fedf27b6de76c8a13e2db050d0a7bd905@95.216.42.83:26656,8ef9baeaaf8e4e3c478c74b2334ab61d7190be72@91.144.158.116:46656,fb68cab9ec9154edc636dccfa405ba560d22ace7@217.76.49.187:26656,5464a7a1982d527844ee93a9d9c24e478c4e09ed@34.29.69.27:26656,acc3fe0b067e10b55c060b2f740d6193bf15a315@15.204.207.179:26656,46b4d74ffcbf709d5b5e0f9c653355d3d86804cb@45.87.2.247:26656,bda935167c4ffaaf4841b59abd192b49165114f3@193.46.243.125:26656,0adbe1e790b58d19cc53a9839059a95d7d5d7aba@65.109.70.23:19956,433be6210ad6350bebebad68ec50d3e0d90cb305@217.13.223.167:60856,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656,88023a76785c2f1d7a3d6ce2c48713c5ba94e47b@65.109.82.249:36656,fb2bf1c6d29f7cc92f3ffba5fc6ab546d4662ef5@113.172.36.141:26656,8d7df5eb69f080a324b96bbd604ef49884406b46@38.242.136.251:26656,bf7aef75c35725f89f31c12197100a1dd91b3174@146.190.47.103:26656,3c47fd1662bcb17a4713c23e41d7b25e34478b8e@103.19.25.157:26672,d3eb474a1f90d004e49638e384069c32d7dcc8a2@185.252.232.110:26656,2031e65ee8a13e57d922a14d28d67be0ada21a95@54.194.240.43:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
