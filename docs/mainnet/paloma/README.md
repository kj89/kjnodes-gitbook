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

**live-peers** (16)
```bash
peers="ef1cd7da8319351b51ec930924929d03a5b76dc3@65.108.225.57:26656,8ed8cddfac504d986a2c6545def0e57b2c6aa5db@65.109.106.172:38656,ab6875bd52d6493f39612eb5dff57ced1e3a5ad6@95.217.229.18:10656,99c890c97afc8abfdfeff662d539af5c504a0baf@88.99.67.234:26656,b244dfc19293103040d4bdad359534d0990a9070@45.140.185.181:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:10656,22e7a98b54070bee0f504305d9ed0fb7a2b24ab6@34.221.60.207:26656,7fc87c698d58bcbd1c6092f951d5f150eed05744@138.201.156.255:26656,8af8dfa817359036f55f6793b0ed4bcce8884027@85.14.245.70:26656,f4c43099e04b721c54a454dad85f61da49be90bc@65.108.199.222:28656,b92c94f00b46500a5ff8920acd438c0873c2f9da@50.116.13.101:26656,1a0232b9426aa1c7a78c92a2136b69d050bb6942@65.108.224.126:26656,874ccf9df2e4c678a18a1fb45a1d3bb703f87fa0@65.109.172.249:26656,527200c42834243b6dc8dacbe26423b7e6577e0f@138.201.129.102:26656,6ee0ed8ddb1eaaf095686962d71fddb1383b5199@65.21.138.123:26656,5321570794c61a8285505812cb7ebd6308a86583@65.109.113.253:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.paloma/config/config.toml
```
