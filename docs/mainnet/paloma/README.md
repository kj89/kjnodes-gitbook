# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/paloma.png" width="150" alt=""><figcaption></figcaption></figure>

Paloma is a fast, permissionless, Cosmos-SDK blockchain that  moves messages securely, between any other blockchains.

**Chain ID**: messenger | **Latest Version Tag**: v0.11.6 | **Wasm**: ON

[Website](https://www.palomachain.com) | [Discord](https://discord.gg/tKVFpfdSw4) | [Twitter](https://twitter.com/paloma_chain)




## Chain explorer
[https://explorer.kjnodes.com/paloma](https://explorer.kjnodes.com/paloma)

## Public endpoints

* api: [https://paloma.api.kjnodes.com](https://paloma.api.kjnodes.com)
* rpc: [https://paloma.rpc.kjnodes.com](https://paloma.rpc.kjnodes.com)
* grpc: [https://paloma.grpc.kjnodes.com](https://paloma.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@paloma.rpc.kjnodes.com:10656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@paloma.rpc.kjnodes.com:10659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/paloma/addrbook.json > $HOME/.paloma/config/addrbook.json
```

**live-peers** (13)
```bash
peers="874ccf9df2e4c678a18a1fb45a1d3bb703f87fa0@65.109.172.249:26656,15f4b11b50810b5046679a12b494e42a2c9034fd@65.109.30.12:26656,317141e329bc214a76ba92201f6818574ebe5323@135.181.114.98:36656,1a0232b9426aa1c7a78c92a2136b69d050bb6942@65.108.224.126:26656,7fc87c698d58bcbd1c6092f951d5f150eed05744@138.201.156.255:26656,60066422d3b70fbf7571012b267dc2cccd9603d5@149.102.156.223:26656,16f0d09580054101394ea08bbb48b1ad5bb91a27@95.214.52.144:10656,22e7a98b54070bee0f504305d9ed0fb7a2b24ab6@34.221.60.207:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:10656,06e9c9d5c07755d36241249a568b51ec8476fe65@135.181.220.168:26656,f4c43099e04b721c54a454dad85f61da49be90bc@65.108.199.222:28656,106350c704aa5e2e0af1464cd3269372d86a9b24@148.113.137.33:26656,b92c94f00b46500a5ff8920acd438c0873c2f9da@50.116.13.101:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.paloma/config/config.toml
```
