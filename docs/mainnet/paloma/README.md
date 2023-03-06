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

**live-peers** (22)
```bash
peers="98b54cd6696e616fe966008ebf2bac409e3e0773@65.108.194.44:26656,06e9c9d5c07755d36241249a568b51ec8476fe65@135.181.220.168:26656,317141e329bc214a76ba92201f6818574ebe5323@135.181.114.98:36656,ef1cd7da8319351b51ec930924929d03a5b76dc3@65.108.225.57:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:10656,7e93f6409ade895fe301b502d6fb9dfb96343a34@135.125.5.34:54056,9cf215d69773173a4c40eb2e811cea8aa7e37432@213.239.216.252:21656,471a09da6fafb67bff3aa1f01e00fd1830e53262@136.243.94.138:26656,dfa0d66a3713bf6b49bc509a2a4fc75bee042a30@23.88.77.188:20009,e833844c00b8ce60ce6826f170becfa18e6172c2@46.4.27.59:26656,7eae755c119f538e0dc99f3c37289de628bc9526@209.182.239.169:26656,124cbe860f1eaa8084444587928db17c78ebd8f3@34.147.54.231:26656,e4b7cdd48c39c355e9a3480f4f4d5afab8fb0e08@46.0.203.78:26637,cb8a1e9e12ac06dbd565311137f6c93d66fd96f8@104.167.221.18:26656,22e7a98b54070bee0f504305d9ed0fb7a2b24ab6@34.221.60.207:26656,b92c94f00b46500a5ff8920acd438c0873c2f9da@50.116.13.101:26656,8af8dfa817359036f55f6793b0ed4bcce8884027@85.14.245.70:26656,16f0d09580054101394ea08bbb48b1ad5bb91a27@95.214.52.144:10656,9581fadb9a32f2af89d575bb0f2661b9bb216d41@46.4.23.108:26656,15f4b11b50810b5046679a12b494e42a2c9034fd@65.109.30.12:26656,31177b544fcf1cae76e3560812f4f901cab27126@65.109.61.175:26656,b244dfc19293103040d4bdad359534d0990a9070@45.140.185.181:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.paloma/config/config.toml
```
