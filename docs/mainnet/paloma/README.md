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
peers="317141e329bc214a76ba92201f6818574ebe5323@135.181.114.98:36656,ef1cd7da8319351b51ec930924929d03a5b76dc3@65.108.225.57:26656,5321570794c61a8285505812cb7ebd6308a86583@65.109.113.253:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:10656,7eae755c119f538e0dc99f3c37289de628bc9526@209.182.239.169:26656,471a09da6fafb67bff3aa1f01e00fd1830e53262@136.243.94.138:26656,106350c704aa5e2e0af1464cd3269372d86a9b24@148.113.137.33:26656,22e7a98b54070bee0f504305d9ed0fb7a2b24ab6@34.221.60.207:26656,e833844c00b8ce60ce6826f170becfa18e6172c2@46.4.27.59:26656,53f37ac93aec70dea3abc40108f42a00877b4665@64.227.142.91:26656,99c890c97afc8abfdfeff662d539af5c504a0baf@88.99.67.234:26656,b9a89009ceb27a55295f95f6f6ef14a2f68b627e@190.15.196.193:26656,b89bec4b3fccbb6928c376ad2e2c38e3b59832ec@78.185.11.68:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.paloma/config/config.toml
```
