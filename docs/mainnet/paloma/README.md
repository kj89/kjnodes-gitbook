# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/paloma.png" width="150" alt=""><figcaption></figcaption></figure>

Paloma is a fast, permissionless, Cosmos-SDK blockchain that  moves messages securely, between any other blockchains.

**Chain ID**: messenger | **Latest Version Tag**: v0.11.6 | **Wasm**: ON

[Website](https://www.palomachain.com) | [Discord](https://discord.gg/tKVFpfdSw4) | [Twitter](https://twitter.com/paloma_chain)



Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/paloma](https://explorer.kjnodes.com/paloma)

## Public endpoints

* api: [https://paloma.api.kjnodes.com](https://paloma.api.kjnodes.com)
* rpc: [https://paloma.rpc.kjnodes.com](https://paloma.rpc.kjnodes.com)
* grpc: paloma.grpc.kjnodes.com:10090

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
peers="ab6875bd52d6493f39612eb5dff57ced1e3a5ad6@95.217.229.18:10656,5321570794c61a8285505812cb7ebd6308a86583@65.109.113.253:26656,942951ad44b974098db48432455f135a653edbb1@65.21.230.230:31656,7e93f6409ade895fe301b502d6fb9dfb96343a34@135.125.5.34:54056,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:10656,41a47bae18f81c1f626e4b238221b77e274424d7@45.33.65.223:26656,b92c94f00b46500a5ff8920acd438c0873c2f9da@50.116.13.101:26656,9581fadb9a32f2af89d575bb0f2661b9bb216d41@46.4.23.108:26656,08c242d4505c5db223647069fdc0acb6e90079aa@65.109.106.214:26656,e833844c00b8ce60ce6826f170becfa18e6172c2@46.4.27.59:26656,f4c43099e04b721c54a454dad85f61da49be90bc@65.108.199.222:28656,b9a89009ceb27a55295f95f6f6ef14a2f68b627e@190.3.117.147:26656,dfa0d66a3713bf6b49bc509a2a4fc75bee042a30@23.88.77.188:20009,4a0b3275453e3a12fca3214268ac865689c90a8e@135.181.76.35:46656,87b4221770495e66e772a53bbea92a15aff288c2@144.126.158.0:26656,60066422d3b70fbf7571012b267dc2cccd9603d5@149.102.156.223:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.paloma/config/config.toml
```
