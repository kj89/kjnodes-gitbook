# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/paloma.png" width="150" alt=""><figcaption></figcaption></figure>

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

**live-peers** (24)
```bash
peers="317141e329bc214a76ba92201f6818574ebe5323@135.181.114.98:36656,527200c42834243b6dc8dacbe26423b7e6577e0f@138.201.129.102:26656,4569193b58dfc6d9ca9acd4e2bcabf596e5b6b3c@65.21.7.251:10656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:10656,98b54cd6696e616fe966008ebf2bac409e3e0773@65.108.194.44:26656,874ccf9df2e4c678a18a1fb45a1d3bb703f87fa0@65.109.172.249:26656,7e93f6409ade895fe301b502d6fb9dfb96343a34@135.125.5.34:54056,7eae755c119f538e0dc99f3c37289de628bc9526@209.182.239.169:26656,9cf215d69773173a4c40eb2e811cea8aa7e37432@213.239.216.252:21656,b41423c8b181c3f2c47df39cca12e7d9bfcfd75e@213.239.215.77:21656,471a09da6fafb67bff3aa1f01e00fd1830e53262@136.243.94.138:26656,99c890c97afc8abfdfeff662d539af5c504a0baf@88.99.67.234:26656,22e7a98b54070bee0f504305d9ed0fb7a2b24ab6@34.221.60.207:26656,cb8a1e9e12ac06dbd565311137f6c93d66fd96f8@104.167.221.18:26656,b92c94f00b46500a5ff8920acd438c0873c2f9da@50.116.13.101:26656,ef1cd7da8319351b51ec930924929d03a5b76dc3@65.108.225.57:26656,41a47bae18f81c1f626e4b238221b77e274424d7@144.126.158.0:26656,e833844c00b8ce60ce6826f170becfa18e6172c2@46.4.27.59:26656,810bea15ec11d510dd33170851ee2ab74c48b6de@81.0.221.57:26656,e4b7cdd48c39c355e9a3480f4f4d5afab8fb0e08@46.0.203.78:26637,9581fadb9a32f2af89d575bb0f2661b9bb216d41@46.4.23.108:26656,16f0d09580054101394ea08bbb48b1ad5bb91a27@95.214.52.144:10656,d44dcdbc4d0f5ae1415143a80f9e5d092af68819@188.165.205.120:10656,124cbe860f1eaa8084444587928db17c78ebd8f3@149.90.94.145:26658"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.paloma/config/config.toml
```
