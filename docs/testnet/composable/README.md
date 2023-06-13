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
peers="9a8b06a3b594fdbceaeeaf3d46aa97d302ed0303@185.255.131.27:26656,a3ddd1ffc5d24bd12fc4b2af5d2769776f5ce67d@65.109.92.240:21206,ab771b5501a129c0d26cdef4bd3db1638702a24b@65.109.99.156:26656,1f3bc143690c465800406a7b6c2898d4f0adebe6@65.21.91.160:27111,9ae49a070ea985784830da8050769ad6791caef5@164.92.64.61:15956,e9441db297752fb454f63d7f0f0c8eb5e067d528@34.124.143.97:26656,638ae5071bd03e35c90e90c11a57c580d80cde0c@81.5.117.14:15956,783e682b38c0565082fe5d897b24feebf687c52b@65.108.13.154:37656,c866bd14649bb402dcb08c861add820b152e39e3@173.212.233.177:15956,3461731f09871909987fa3df99c9ac623ea303b3@207.180.241.219:26656,f306956520010c5ddd0e67c69f61f1de3fa91552@88.198.52.46:22256,022221b7dc3be873a5b7b24682154f32c07e96cc@194.163.167.138:52656,c241d021004ad9b0fe7fa2d967ff9f1f3b20c1f0@136.243.172.166:15956,e083e1ee42159e3b57284d38530efc29c6f8a4c9@109.123.247.105:26656,2a9225e33a3cd40d4f9118a111a463e4c11bc6c2@31.220.85.1:26656,117dea3045bce3a1bc4b0b59ed01a9be88df6815@65.108.124.121:60656,13d2379fc4d36fe6829c316cf3fdfd7d62c59f7c@194.34.232.150:15956,8be7bfa6c270469971875cb6f23c957402654a14@207.180.194.162:26656,5a331fc6afa9ae7cbd6c9ebf39358161052c962b@65.109.65.248:37656,c0f197bdf6c4a4a16eb9db112d1ec9545336fd43@168.119.91.22:2250,4491f06f803252917d69d053ed85adba5ad17474@5.166.240.95:15956,3351847a55dd16faf533f3a02caba9610cc87320@158.220.100.228:27656,b2ab46fe515d0ede14bbe37b16a24bfdf67c8a5b@167.235.7.34:56656,76bde904c1f177a2c8c1123150073be38c27ad5f@75.119.146.244:26656,3bab9d5cfb23118e703e1c4b62820f35acf45521@144.76.174.27:26656,ca1d4fd9037ad49a37976fa4bdfcce7f4329857f@158.101.110.160:26656,904c32b57803fbcf20ec15de02ee076c54c5f35a@185.217.126.187:15956,6b792ff5118ef1e141085af62ace3ad846d757b4@193.34.212.165:26656,f4078136bacf232ff67c4ab0fdbe5c88fb1f2f94@31.220.72.179:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15956"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.banksy/config/config.toml
```
