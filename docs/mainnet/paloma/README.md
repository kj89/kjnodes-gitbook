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

**live-peers** (14)
```bash
peers="98b54cd6696e616fe966008ebf2bac409e3e0773@65.108.194.44:26656,7eae755c119f538e0dc99f3c37289de628bc9526@209.182.239.169:26656,9cf215d69773173a4c40eb2e811cea8aa7e37432@213.239.216.252:21656,dfa0d66a3713bf6b49bc509a2a4fc75bee042a30@23.88.77.188:20009,7fc87c698d58bcbd1c6092f951d5f150eed05744@138.201.156.255:26656,124cbe860f1eaa8084444587928db17c78ebd8f3@34.147.54.231:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:10656,22e7a98b54070bee0f504305d9ed0fb7a2b24ab6@34.221.60.207:26656,874ccf9df2e4c678a18a1fb45a1d3bb703f87fa0@65.109.172.249:26656,8af8dfa817359036f55f6793b0ed4bcce8884027@85.14.245.70:26656,b92c94f00b46500a5ff8920acd438c0873c2f9da@50.116.13.101:26656,60066422d3b70fbf7571012b267dc2cccd9603d5@149.102.156.223:26656,f4c43099e04b721c54a454dad85f61da49be90bc@65.108.199.222:28656,106350c704aa5e2e0af1464cd3269372d86a9b24@148.113.137.33:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.paloma/config/config.toml
```
