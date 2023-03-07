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

**live-peers** (42)
```bash
peers="a884387139109784cad9193652b82ef20a85d713@38.242.159.148:26656,ee4db669ed2ff87cb2a47f848fa061517eb47737@161.97.151.46:26656,3df5a68b919177179c6dcb0b9c9354fd6bbba1c8@65.109.92.240:20116,297bf784ea674e05d36af48e3a951de966f9aa40@65.109.34.133:36656,7f2828e3910a4b165a65e5bfb2465c1e809bad3b@65.108.48.182:26656,1fefb6b75431482502e125a290deba1e7e539d4e@135.181.148.11:26656,eb503dddcc41ba801c646d63cc762de4e9c43aa4@35.228.23.164:26656,ba56c564a5430632e59e2b08fc348735bc56b32f@154.12.232.140:26656,927a323649e7dd8d4c75da6e5edaee439652b46f@65.109.92.241:20116,56158e0f2acf850114e82644afceb565a73b08cc@185.144.99.95:26656,48a2a7762a579d25bca95b0a3548b714238dd60b@213.239.216.252:20656,0833039f717227ccd156d156ea772746b8ac6d71@146.19.24.139:26656,90b1d14fc7393c6b6452ecf8b3cdd078a445a238@65.109.112.178:29656,6771e65c1b30cc514faf5943320fdda480fe9124@95.216.39.183:26656,23ff658b56fbb8bc73372973a34733ff5d79b435@142.132.202.50:11604,073a2d6ef69f04b563e160a0e33eab84ae093aa9@154.26.157.233:35656,230d299006a432b0f44534ca8a19c8c876c0ccb3@85.10.193.246:26656,24e894d4d8a18276acf6051cccf369a1ce69842d@65.108.151.105:26656,2d13d679b64e1a574904a140f72815644ec71131@65.21.133.125:30656,a6150d39e4725d28a56f41ebf3c6d457c54bd2f1@34.138.250.4:26656,32a8eec046b95e8646ff0810b4596dc7083a0beb@65.108.145.131:26656,59af99085c961a6a5c8dc4bc8b3abffda16ddccb@135.181.38.62:26656,b1c07038b5b9b96d6fb35e4bb417af7ed238e733@95.217.35.186:26656,6fad54232f11a0306bd0d942c2ec5f9ba0ae2f1a@34.91.54.209:26656,b9e8ec4eeb359e1b3cf5675563e72787b9d40adf@95.217.132.146:26656,d7ac44bf8f8d760c3df1a8695145021f35feb985@34.88.220.124:26656,4034efbff7c82e1a2d3908fefd2512552dea63f5@65.109.38.208:26651,ed145a35b436878c1f1c10634bd18600f3696e17@95.217.181.142:26656,a6dbf51663c0e4cbfd7dd3965ab8ad022de0952f@154.26.157.230:35656,78e3ef8adf819b479acc13a2f92ab5c0fa350aeb@66.45.231.30:11464,9e288261ac5e42f25bd281f2564d756596aded6c@95.216.7.169:60856,c4428d0ec640829414efff4ae7a793004edad867@154.26.157.228:35656,5034467ea06fed661f02770ca27197d033df71d2@149.102.132.138:35656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:35656,f1b1df46afd4c9d4f66051437078c0b85bc6b67b@65.108.206.118:61056,b5cbe34ca84c76c3301c29dd7858cd90477d078b@149.102.133.73:35656,360d7095f3c1250a013cfe66c43a3f0790782f78@84.46.254.50:26656,90b40d2b773090b82aa7788c2d1937e4fd6d2dc0@65.108.231.124:19656,e576d332451c7c3c0c5c753b1bbd4e670b1ecfc7@5.161.97.83:26656,b72f2156db8c87e679dc853730746ff40038120c@213.239.215.77:26656,0d600b8281ee6a710c213023755d2382cf90af13@116.202.165.116:46656,89d067dc2a046f7b7c1c787740fff18962bf199f@95.165.149.94:29656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.haqqd/config/config.toml
```
