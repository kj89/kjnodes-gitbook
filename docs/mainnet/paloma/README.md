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
peers="317141e329bc214a76ba92201f6818574ebe5323@135.181.114.98:36656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:10656,8ed8cddfac504d986a2c6545def0e57b2c6aa5db@65.109.106.172:38656,9581fadb9a32f2af89d575bb0f2661b9bb216d41@46.4.23.108:26656,16f0d09580054101394ea08bbb48b1ad5bb91a27@95.214.52.144:10656,106350c704aa5e2e0af1464cd3269372d86a9b24@148.113.137.33:26656,7fc87c698d58bcbd1c6092f951d5f150eed05744@138.201.156.255:26656,22e7a98b54070bee0f504305d9ed0fb7a2b24ab6@34.221.60.207:26656,874ccf9df2e4c678a18a1fb45a1d3bb703f87fa0@65.109.172.249:26656,4569193b58dfc6d9ca9acd4e2bcabf596e5b6b3c@65.21.7.251:10656,6ee0ed8ddb1eaaf095686962d71fddb1383b5199@65.21.138.123:26656,1a0232b9426aa1c7a78c92a2136b69d050bb6942@65.108.224.126:26656,9cf215d69773173a4c40eb2e811cea8aa7e37432@213.239.216.252:21656,d73f7f6de427369a60245725047f49b1fd0e0a2f@65.108.199.26:31656,999dd829036eb4a2c4024b0d35d0fa7c02562770@84.54.23.3:34656,60066422d3b70fbf7571012b267dc2cccd9603d5@149.102.156.223:26656,08c242d4505c5db223647069fdc0acb6e90079aa@65.109.106.214:26656,f4c43099e04b721c54a454dad85f61da49be90bc@65.108.199.222:28656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.paloma/config/config.toml
```
