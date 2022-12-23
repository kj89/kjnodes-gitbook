# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/defund.png" width="150" alt=""><figcaption></figcaption></figure>

DeFund is an L1 blockchain built for building decentralized permissionless,  on-chain trading strategies that are packaged into a dETF (decentralized  exchange-traded fund) token, tradable within any ecosystem or CEX.

**Chain ID**: defund-private-3 | **Latest Version Tag**: v0.2.1 | **Wasm**: OFF

[Website](https://www.defund.app) | [Discord](https://discord.gg/FV26pRPZ3P) | [Twitter](https://twitter.com/defund_finance)


## Public endpoints

* rpc: [https://defund-testnet.rpc.kjnodes.com](https://defund-testnet.rpc.kjnodes.com)
* api: [https://defund-testnet.api.kjnodes.com](https://defund-testnet.api.kjnodes.com)

## Peering

**state-sync**

```
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@defund-testnet.rpc.kjnodes.com:40656
```

**seed-node**

```
3f472746f46493309650e5a033076689996c8881@defund-testnet.rpc.kjnodes.com:40659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/defund-testnet/addrbook.json > $HOME/.defund/config/addrbook.json
```

**live-peers** (32)
```
peers="9f4ea4b9da9801ba5e97924d13c7c793d94bfec9@45.147.199.176:26656,68b4a53b3b67da6a4736888c36074eb316ea510d@75.119.157.222:26656,fb5f99d34d60511d947ee077ef33005e438d0c0f@185.202.223.160:26656,b9a22be1f13a4ed99de4ecdd4c9e2a9e4711c2ac@45.147.199.190:26656,ad35b87df11c37b5f66931cd86c5dc2853aabae2@95.216.69.88:36656,bd90b1dd4ae3636e5f452be51b8e75ca104b5bfc@109.123.247.53:40656,a713c7dbfbcf0704f591bcc07d1f116303c44b27@45.87.0.238:26656,d1976601f04df2a2c7e35c0e8212464acfb7512e@75.119.147.235:26656,0a8430b93bd3ddbf247388ca638512981ff07eaf@195.3.220.9:26656,f868bc6debc472df810792e22ebeeb8d8e95f094@89.58.45.204:60756,4c291b33574d679e43f7cec340ba4befecec0724@161.97.152.115:26656,188bb4f06a978ec964105bb332276a674854da02@109.123.252.161:26656,57eadf177e7429db82bfdbed6fa0521e8741e404@94.130.13.40:26656,20151f8b15d6f3ad670f5bfc1c747de72e96fb3f@194.180.176.128:26656,9160044d4a2778b66451b424ab9dff19d99abf4d@194.104.136.101:26656,a78c5a1fa7b12eef729fa3dec3b7c3b073552664@45.147.199.191:26656,4c170418a04a65b74fb17880aaa25674aae1451f@23.111.154.14:26651,8dd498377306dcdfca367e848ed66a9453ccc1fc@95.217.214.142:26666,00ddc480c7373130e1086c54173ce2bc5e0e2d45@185.190.140.81:40656,71f8ad83e61fdf543539445208623db5e8e0399f@95.216.208.183:26656,219c417bd9de04c60f730abd4769e981f10c083b@109.123.249.191:26656,f329bee02e530e05a8937887c8ea4e75851281f1@194.180.176.126:26656,0b141f72551552a5faf109413292e72408a34c34@65.109.27.156:32656,edabbcbfb21c488be785f0925b0060c717440bad@92.119.112.229:26656,e9d046b2248e07896dce1bcc5faff02d65745332@95.111.254.87:36656,4d3b782ab389525370f53d40e970b1362bc92106@185.182.186.202:26656,18921a27facf3760d59147e4ae176b1bdf226346@195.201.237.172:18656,d31d9801e7a021d287570b94ffcf27b91b0d9b66@217.76.55.74:26656,95d487c4f51295c4cd799cc7fe53d23ea7298bdf@206.246.71.251:46656,544266471d3da917f0b6cf3b65f9d437d62134e8@157.90.252.194:26666,fd3f439c775df4a7c1ced33d613124acee4187a6@194.163.154.129:40656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.defund/config/config.toml
```
