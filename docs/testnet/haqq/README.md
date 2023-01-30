# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/haqq.png" width="150" alt=""><figcaption></figcaption></figure>

Haqq is the blockchain network that issues Islamic Coin,  its native cryptocurrency. Haqq is fast, trusted and  compatible with thousands of applications around the world.

**Chain ID**: haqq_54211-3 | **Latest Version Tag**: v1.3.0 | **Wasm**: OFF

[Website](https://islamiccoin.net) | [Discord](https://discord.gg/hU9MHG5kZq) | [Twitter](https://twitter.com/Islamic_Coin)


## Chain explorer
[https://explorer.kjnodes.com/haqq-testnet](https://explorer.kjnodes.com/haqq-testnet)

## Public endpoints

* api: [https://haqq-testnet.api.kjnodes.com](https://haqq-testnet.api.kjnodes.com)
* rpc: [https://haqq-testnet.rpc.kjnodes.com](https://haqq-testnet.rpc.kjnodes.com)
* grpc: [https://haqq-testnet.grpc.kjnodes.com](https://haqq-testnet.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@haqq-testnet.rpc.kjnodes.com:35656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@haqq-testnet.rpc.kjnodes.com:35659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/haqq-testnet/addrbook.json > $HOME/.haqqd/config/addrbook.json
```

**live-peers** (31)
```bash
peers="51e4544568cf880451bfffc292de88adc472f0e0@34.147.126.38:26656,360d7095f3c1250a013cfe66c43a3f0790782f78@84.46.254.50:26656,7f2828e3910a4b165a65e5bfb2465c1e809bad3b@65.108.48.182:26656,70c1b8334bf08fe5d56fb53d07da11f01faa560b@65.109.30.90:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:35656,56158e0f2acf850114e82644afceb565a73b08cc@185.144.99.95:26656,6771e65c1b30cc514faf5943320fdda480fe9124@95.216.39.183:26656,23ff658b56fbb8bc73372973a34733ff5d79b435@142.132.202.50:11604,0833039f717227ccd156d156ea772746b8ac6d71@146.19.24.139:26656,2d13d679b64e1a574904a140f72815644ec71131@65.21.133.125:30656,f54d4de6d4ae81ec8a2315b54247872b315f198d@65.109.57.9:26656,b1c07038b5b9b96d6fb35e4bb417af7ed238e733@95.217.35.186:26656,ed145a35b436878c1f1c10634bd18600f3696e17@95.217.181.142:26656,32a8eec046b95e8646ff0810b4596dc7083a0beb@65.108.145.131:26656,ff6df373bf7bce436d488d2d8f5f5b283c6431d4@51.79.100.160:26656,24e894d4d8a18276acf6051cccf369a1ce69842d@65.108.151.105:26656,dddce0afadf33e8b8c33a9e797493cd18a9ce5c7@154.26.157.240:35656,922d76c72392b5b69c03a4ae56b3aba544ff1139@144.126.194.175:26656,d59dc597f0d41bcbc7ff53374686affb143726c2@51.195.203.103:35656,0629018cef2e53288757381ffdc0b84cbb5931cc@95.216.1.249:26656,f57fae1bdea281392b563a58978a2d8c0a37725f@95.217.233.234:26656,48a2a7762a579d25bca95b0a3548b714238dd60b@213.239.216.252:20656,90b40d2b773090b82aa7788c2d1937e4fd6d2dc0@65.108.231.124:19656,927a323649e7dd8d4c75da6e5edaee439652b46f@65.109.92.241:20116,5a223d77d01319a8c7f648eddfc8549cafcd8ca5@34.147.118.211:26656,bb6c75744906248c25c65291b0f48637f11357fe@109.123.252.231:35656,00b1befaceba6b0178d2b6076ae0968adf4bd7b5@65.108.67.152:26656,3df5a68b919177179c6dcb0b9c9354fd6bbba1c8@65.109.92.240:20116,f6c7d753cc4544031e8e243841f687cae3f09abe@161.97.145.34:35656,65bfa4b4b4b9accb9c0e0d46a1c07ae9a44a3a23@168.119.227.142:26656,62bf004201a90ce00df6f69390378c3d90f6dd7e@45.83.173.19:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.haqqd/config/config.toml
```
