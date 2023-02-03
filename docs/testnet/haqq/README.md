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

**live-peers** (34)
```bash
peers="51e4544568cf880451bfffc292de88adc472f0e0@34.147.126.38:26656,2d13d679b64e1a574904a140f72815644ec71131@65.21.133.125:30656,b09a7df87767ae782099d5ee352d679e3260247a@65.108.124.219:34656,7f2828e3910a4b165a65e5bfb2465c1e809bad3b@65.108.48.182:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:35656,56158e0f2acf850114e82644afceb565a73b08cc@185.144.99.95:26656,23ff658b56fbb8bc73372973a34733ff5d79b435@142.132.202.50:11604,6771e65c1b30cc514faf5943320fdda480fe9124@95.216.39.183:26656,1c5a4624a7f1a71e240ae2df82e97d5e9f46ff5c@88.99.214.188:60956,ff6df373bf7bce436d488d2d8f5f5b283c6431d4@51.79.100.160:26656,3df5a68b919177179c6dcb0b9c9354fd6bbba1c8@65.109.92.240:20116,00b1befaceba6b0178d2b6076ae0968adf4bd7b5@65.108.67.152:26656,8558de1d3062319bb877316c5c33e704f1e0a972@84.46.242.147:26656,32a8eec046b95e8646ff0810b4596dc7083a0beb@65.108.145.131:26656,24e894d4d8a18276acf6051cccf369a1ce69842d@65.108.151.105:26656,d59dc597f0d41bcbc7ff53374686affb143726c2@51.195.203.103:35656,360d7095f3c1250a013cfe66c43a3f0790782f78@84.46.254.50:26656,43dc2d5ab6fa30cb10959717d26f31bc45b56fdd@149.102.133.67:35656,78e3ef8adf819b479acc13a2f92ab5c0fa350aeb@66.45.231.30:11464,90b40d2b773090b82aa7788c2d1937e4fd6d2dc0@65.108.231.124:19656,ed145a35b436878c1f1c10634bd18600f3696e17@95.217.181.142:26656,a884387139109784cad9193652b82ef20a85d713@38.242.159.148:26656,9444cf6e8cc3e452f8006acce0283d87ee663b7a@185.163.125.253:35656,077d5d9169efb4b070ce7895d680a9d2148d522c@195.201.195.40:36656,5a223d77d01319a8c7f648eddfc8549cafcd8ca5@34.147.118.211:26656,bb6c75744906248c25c65291b0f48637f11357fe@109.123.252.231:35656,f57fae1bdea281392b563a58978a2d8c0a37725f@95.217.233.234:26656,d8d8378108d4963ecdbb50e2f1712bc6f785f52c@154.26.157.227:35656,331ca63236ba05842d561e22c0bcc8582efa60a1@209.126.80.192:26656,59af99085c961a6a5c8dc4bc8b3abffda16ddccb@135.181.38.62:26656,64a840f6f5344a22a485b2818f9da9a457d42827@95.217.57.232:36656,6ce864d853904ebef9400528f129d8fefa6f1827@91.211.251.232:36656,4c85cefdf872bcf8839618fd14b854b460e9f615@154.26.157.231:35656,0833039f717227ccd156d156ea772746b8ac6d71@146.19.24.139:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.haqqd/config/config.toml
```
