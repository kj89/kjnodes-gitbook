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
peers="6b792ff5118ef1e141085af62ace3ad846d757b4@193.34.212.165:26656,9a8b06a3b594fdbceaeeaf3d46aa97d302ed0303@185.255.131.27:26656,f75c4ca083ff3ecc40777e63cb9a28d6458d1d1d@207.180.246.161:26616,c0f197bdf6c4a4a16eb9db112d1ec9545336fd43@168.119.91.22:2250,76bde904c1f177a2c8c1123150073be38c27ad5f@75.119.146.244:26656,f4078136bacf232ff67c4ab0fdbe5c88fb1f2f94@31.220.72.179:26656,ab771b5501a129c0d26cdef4bd3db1638702a24b@65.109.99.156:26656,a3ddd1ffc5d24bd12fc4b2af5d2769776f5ce67d@65.109.92.240:21206,b2a5b6c11e7d71c2a43d88a73b9dcff3352f4302@57.128.86.7:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.21:26976,c866bd14649bb402dcb08c861add820b152e39e3@173.212.233.177:15956,3bab9d5cfb23118e703e1c4b62820f35acf45521@144.76.174.27:26656,4491f06f803252917d69d053ed85adba5ad17474@5.166.240.95:15956,783e682b38c0565082fe5d897b24feebf687c52b@65.108.13.154:37656,bc5c4e4d5d4b4a1ab157e5d6907b8ae335aa2183@95.216.213.192:26656,022221b7dc3be873a5b7b24682154f32c07e96cc@194.163.167.138:52656,3461731f09871909987fa3df99c9ac623ea303b3@207.180.241.219:26656,56bb737da7d2628b5c252e992c649489120838c7@65.21.178.202:26656,c241d021004ad9b0fe7fa2d967ff9f1f3b20c1f0@136.243.172.166:15956,9ae49a070ea985784830da8050769ad6791caef5@164.92.64.61:15956,e083e1ee42159e3b57284d38530efc29c6f8a4c9@109.123.247.105:26656,638ae5071bd03e35c90e90c11a57c580d80cde0c@81.5.117.14:15956,8be7bfa6c270469971875cb6f23c957402654a14@207.180.194.162:26656,b2ab46fe515d0ede14bbe37b16a24bfdf67c8a5b@167.235.7.34:56656,9e7270b955791bb00acd68856366ed5450134d29@82.208.22.64:26656,ab2ba40e4f9dff8e09ac1734dce6eba1aa8770a8@65.109.55.186:656,5a331fc6afa9ae7cbd6c9ebf39358161052c962b@65.109.65.248:37656,f6bdd60edcc84f2f02d582dc411cef80c5176df1@38.242.133.188:26656,f306956520010c5ddd0e67c69f61f1de3fa91552@88.198.52.46:22256,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15956"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.banksy/config/config.toml
```
