# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/haqq.png" width="150" alt=""><figcaption></figcaption></figure>

Haqq is the blockchain network that issues Islamic Coin,  its native cryptocurrency. Haqq is fast, trusted and  compatible with thousands of applications around the world.

**Chain ID**: haqq_54211-3 | **Latest Version Tag**: v1.3.1 | **Wasm**: OFF

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

**live-peers** (33)
```bash
peers="65bfa4b4b4b9accb9c0e0d46a1c07ae9a44a3a23@168.119.227.142:26656,b09a7df87767ae782099d5ee352d679e3260247a@65.108.124.219:34656,927a323649e7dd8d4c75da6e5edaee439652b46f@65.109.92.241:20116,1fefb6b75431482502e125a290deba1e7e539d4e@135.181.148.11:26656,b72f2156db8c87e679dc853730746ff40038120c@213.239.215.77:26656,a884387139109784cad9193652b82ef20a85d713@38.242.159.148:26656,56158e0f2acf850114e82644afceb565a73b08cc@185.144.99.95:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:35656,b1c07038b5b9b96d6fb35e4bb417af7ed238e733@95.217.35.186:26656,0833039f717227ccd156d156ea772746b8ac6d71@146.19.24.139:26656,6771e65c1b30cc514faf5943320fdda480fe9124@95.216.39.183:26656,230d299006a432b0f44534ca8a19c8c876c0ccb3@85.10.193.246:26656,6ce864d853904ebef9400528f129d8fefa6f1827@91.211.251.232:36656,073a2d6ef69f04b563e160a0e33eab84ae093aa9@154.26.157.233:35656,70c1b8334bf08fe5d56fb53d07da11f01faa560b@65.109.30.90:26656,23ff658b56fbb8bc73372973a34733ff5d79b435@142.132.202.50:11604,ccff2d110a06e8a76fd1529200d96316eb077007@65.108.78.116:46656,eb503dddcc41ba801c646d63cc762de4e9c43aa4@35.228.23.164:26656,90b1d14fc7393c6b6452ecf8b3cdd078a445a238@65.109.112.178:29656,2d13d679b64e1a574904a140f72815644ec71131@65.21.133.125:30656,a6150d39e4725d28a56f41ebf3c6d457c54bd2f1@34.138.250.4:26656,24e894d4d8a18276acf6051cccf369a1ce69842d@65.108.151.105:26656,32a8eec046b95e8646ff0810b4596dc7083a0beb@65.108.145.131:26656,e2852320297ccdc24407d735eea3db213afa17b5@85.10.199.157:12656,ed145a35b436878c1f1c10634bd18600f3696e17@95.217.181.142:26656,51e4544568cf880451bfffc292de88adc472f0e0@34.147.126.38:26656,6fad54232f11a0306bd0d942c2ec5f9ba0ae2f1a@34.91.54.209:26656,90b40d2b773090b82aa7788c2d1937e4fd6d2dc0@65.108.231.124:19656,f50b6abb555c0d420834860d9a8f499801bb3ae8@135.181.62.222:26656,c4428d0ec640829414efff4ae7a793004edad867@154.26.157.228:35656,3df5a68b919177179c6dcb0b9c9354fd6bbba1c8@65.109.92.240:20116,48a2a7762a579d25bca95b0a3548b714238dd60b@213.239.216.252:20656,3f5110515b76596e05a447fd50e4727eaad00124@188.34.201.77:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.haqqd/config/config.toml
```
