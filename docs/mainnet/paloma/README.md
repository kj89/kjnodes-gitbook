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

**live-peers** (18)
```bash
peers="317141e329bc214a76ba92201f6818574ebe5323@135.181.114.98:36656,31177b544fcf1cae76e3560812f4f901cab27126@65.109.61.175:26656,ef1cd7da8319351b51ec930924929d03a5b76dc3@65.108.225.57:26656,99c890c97afc8abfdfeff662d539af5c504a0baf@88.99.67.234:26656,9581fadb9a32f2af89d575bb0f2661b9bb216d41@46.4.23.108:26656,4e35ce47a8c2654a0cd371a2d1485e157b6ce311@93.190.141.218:26656,60066422d3b70fbf7571012b267dc2cccd9603d5@149.102.156.223:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:10656,7fc87c698d58bcbd1c6092f951d5f150eed05744@138.201.156.255:26656,106350c704aa5e2e0af1464cd3269372d86a9b24@148.113.137.33:26656,22e7a98b54070bee0f504305d9ed0fb7a2b24ab6@34.221.60.207:26656,e833844c00b8ce60ce6826f170becfa18e6172c2@46.4.27.59:26656,cb8a1e9e12ac06dbd565311137f6c93d66fd96f8@104.167.221.18:26656,874ccf9df2e4c678a18a1fb45a1d3bb703f87fa0@65.109.172.249:26656,6ee0ed8ddb1eaaf095686962d71fddb1383b5199@65.21.138.123:26656,8ed8cddfac504d986a2c6545def0e57b2c6aa5db@65.109.106.172:38656,f4c43099e04b721c54a454dad85f61da49be90bc@65.108.199.222:28656,19165f3248f358ded53c3f51cf97a22123560b86@65.109.69.154:38656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.paloma/config/config.toml
```
