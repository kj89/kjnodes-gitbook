# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/composable.png" alt=""><figcaption></figcaption></figure>

The complete infrastructure for cross-chain smart  contracts, applications, and modular functionality.

**Chain ID**: banksy-testnet-3 | **Latest Version Tag**: v3.0.0 | **Wasm**: OFF

[Website](https://www.composable.finance) | [Discord](https://discord.gg/composable) | [Twitter](https://twitter.com/ComposableFin)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/composable-testnet](https://explorer.kjnodes.com/composable-testnet)

## Public endpoints

* api: [https://composable-testnet.api.kjnodes.com](https://composable-testnet.api.kjnodes.com)
* rpc: [https://composable-testnet.rpc.kjnodes.com](https://composable-testnet.rpc.kjnodes.com)
* grpc: composable-testnet.grpc.kjnodes.com:15990

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@composable-testnet.rpc.kjnodes.com:15956
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@composable-testnet.rpc.kjnodes.com:15959
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/composable-testnet/addrbook.json > $HOME/.banksy/config/addrbook.json
```

**live-peers** (30)
```bash
peers="df49f4fee2fe62bc0ca8c27ee0dbae3f0abec98f@46.38.232.86:24656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15956,783e682b38c0565082fe5d897b24feebf687c52b@65.108.13.154:37656,a3ddd1ffc5d24bd12fc4b2af5d2769776f5ce67d@65.109.92.240:21206,33d01ca326bb21c3e02c6f05b9cb530eea93c39d@65.109.23.237:30536,b2ab46fe515d0ede14bbe37b16a24bfdf67c8a5b@167.235.7.34:56656,76bde904c1f177a2c8c1123150073be38c27ad5f@75.119.146.244:26656,3461731f09871909987fa3df99c9ac623ea303b3@207.180.241.219:26656,b2a5b6c11e7d71c2a43d88a73b9dcff3352f4302@57.128.86.7:26656,5a331fc6afa9ae7cbd6c9ebf39358161052c962b@65.109.65.248:37656,c866bd14649bb402dcb08c861add820b152e39e3@173.212.233.177:15956,8be7bfa6c270469971875cb6f23c957402654a14@207.180.194.162:26656,0cde9b12f47913678e4fd6eeed1f93711613baa7@65.108.11.234:15656,9a8b06a3b594fdbceaeeaf3d46aa97d302ed0303@185.255.131.27:26656,e083e1ee42159e3b57284d38530efc29c6f8a4c9@109.123.247.105:26656,2a9225e33a3cd40d4f9118a111a463e4c11bc6c2@31.220.85.1:26656,3351847a55dd16faf533f3a02caba9610cc87320@158.220.100.228:27656,ab2ba40e4f9dff8e09ac1734dce6eba1aa8770a8@65.109.55.186:656,c241d021004ad9b0fe7fa2d967ff9f1f3b20c1f0@136.243.172.166:15956,ab771b5501a129c0d26cdef4bd3db1638702a24b@65.109.99.156:26656,05ec13f804da91036f413ca57a61849c169acda3@195.3.223.182:15956,4491f06f803252917d69d053ed85adba5ad17474@5.166.240.95:15956,f6bdd60edcc84f2f02d582dc411cef80c5176df1@38.242.133.188:26656,638ae5071bd03e35c90e90c11a57c580d80cde0c@81.5.117.14:15956,f4078136bacf232ff67c4ab0fdbe5c88fb1f2f94@31.220.72.179:26656,211bebc24e286a973d3038f2fbbf5f673badc190@51.250.4.215:27656,99004e3251209542b30c7502a7c35b1d574cd3ae@195.3.221.16:26656,ca1d4fd9037ad49a37976fa4bdfcce7f4329857f@158.101.110.160:26656,790b9221fd5e05957fba1fe186e3a0a6972ff7d6@65.109.99.216:15956,8f912ac69f9e36f7db9ec98879062f25b010484d@203.96.179.106:36656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.banksy/config/config.toml
```
