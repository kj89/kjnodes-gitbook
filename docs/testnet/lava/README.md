# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/lava.png" width="150" alt=""><figcaption></figcaption></figure>

Lava powers a trustless market for RPC data access. The protocol  governs over peer to peer and private Provider-Application pairings,  ensuring high quality RPC service while creating consensus around data served.

**Chain ID**: lava-testnet-1 | **Latest Version Tag**: v0.4.4 | **Wasm**: OFF

[Website](https://lavanet.xyz) | [Discord](https://discord.com/invite/Tbk5NxTCdA) | [Twitter](https://twitter.com/lavanetxyz)


## Chain explorer
[https://explorer.kjnodes.com/lava-testnet](https://explorer.kjnodes.com/lava-testnet)

## Public endpoints

* api: [https://lava-testnet.api.kjnodes.com](https://lava-testnet.api.kjnodes.com)
* rpc: [https://lava-testnet.rpc.kjnodes.com](https://lava-testnet.rpc.kjnodes.com)
* grpc: [https://lava-testnet.grpc.kjnodes.com](https://lava-testnet.grpc.kjnodes.com)

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

**live-peers** (34)
```bash
peers="dfa93668152cb6b3a822c987f9c22110a1c2f314@178.18.255.221:26656,24a2bb2d06343b0f74ed0a6dc1d409ce0d996451@188.40.98.169:27656,eb7832932626c1c636d16e0beb49e0e4498fbd5e@65.108.231.124:20656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656,3c47fd1662bcb17a4713c23e41d7b25e34478b8e@103.19.25.157:26672,2031e65ee8a13e57d922a14d28d67be0ada21a95@3.252.208.167:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@185.16.39.172:27066,e593c7a9ca61f5616119d6beb5bd8ef5dd28d62d@34.246.190.1:26656,72aabf4950afe5f2514cff8dc6c2c56600e7ed03@34.251.254.15:26656,22c51515eea1df09dc872dc8843efb7fc73770b1@199.175.98.102:26656,f9f49cc8ffbdee85fb8a9551f644f5554a610ebe@91.107.137.90:26656,3a445bfdbe2d0c8ee82461633aa3af31bc2b4dc0@3.252.219.158:26656,d53f227f0682ec552ae1932de2547fa717119253@95.216.102.235:39043,c13b120d588c86008dc4ea5e3633b93c01831124@80.79.5.171:31656,f30d07170a092f82702e3c12334fa9fd828b71c6@168.119.124.130:47656,14ae45e7f2ff7491cfa686a8fcac7cc095bc38ff@213.239.217.52:39656,e77d76e89ae593411ca6a6f1f13bc98d3bdb2024@161.97.142.90:26656,1dc8db6b9b800deded531bfb56ce12defbc98c74@173.249.46.50:26656,0314d53cc790860fb51f36ac656a19789800ce5c@176.103.222.20:26656,433be6210ad6350bebebad68ec50d3e0d90cb305@217.13.223.167:60856,dc1c37e340a191ac0eea7c561b4a3c8fba2ce80a@65.21.237.241:26656,d927303d07abf24b72f3eb8ae495ac02372e3908@91.195.101.78:26656,4f1d528b0beab01ea02d7e3172381f72fae4c616@62.171.129.27:26656,82b5c1c318052440fc9f96336e296610f2cf9f87@65.109.164.110:33656,a5c1d2e86c2dc0eecb009dc71c92d6b5e193db6b@35.210.166.150:26656,0a78dd75926983ba06de451480673487ffa1bcc1@199.175.98.106:26656,40046fe63bdaa9efde27707b0d3de0bf84fedf80@86.111.48.158:26656,6d7ead316f354a549fe22f5ebe72d68ec0af685a@194.233.68.136:44656,563bf40de5ff5d2aa2dc8c4bab350c67bfcb4284@109.123.253.103:26656,bcc19c4f7c3007aea90e24f2fe3a80cef985fee3@89.106.206.190:26656,06ef861547a735da1b649e87e23c0d91ed8379ab@84.54.23.251:26656,377370216f2c003b9d00118ec5373ed21f13aab3@185.16.39.19:35656,5676c8606f23471e220f8bf7317498a61bb93194@65.21.134.202:26686,7e68edc23e6c716b3248099dd1f03810a57975ef@65.109.92.150:34656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
